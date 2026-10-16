// Melhoria progressiva: conteúdo e âncoras permanecem no HTML estático.
document.documentElement.classList.add('has-js');
const motion = window.matchMedia('(prefers-reduced-motion: reduce)');
const menuToggle = document.querySelector('#menu-toggle');
const mobileMenu = document.querySelector('#mobile-menu');
function closeMenu(restoreFocus = false) {
  if (menuToggle.getAttribute('aria-expanded') !== 'true') return;
  mobileMenu.hidden = true;
  menuToggle.setAttribute('aria-expanded', 'false');
  menuToggle.setAttribute('aria-label', 'Abrir menu');
  if (restoreFocus) menuToggle.focus({ preventScroll: true });
}
menuToggle.addEventListener('click', () => {
  const opening = mobileMenu.hidden;
  mobileMenu.hidden = !opening;
  menuToggle.setAttribute('aria-expanded', String(opening));
  menuToggle.setAttribute('aria-label', opening ? 'Fechar menu' : 'Abrir menu');
});
mobileMenu.addEventListener('click', event => {
  const link = event.target.closest('a');
  if (link) {
    closeMenu();
    const href = link.getAttribute('href');
    const destination = href?.startsWith('#') ? document.getElementById(href.slice(1)) : null;
    if (destination) { destination.setAttribute('tabindex', '-1'); destination.focus({ preventScroll: true }); }
  }
});
document.addEventListener('keydown', event => { if (event.key === 'Escape') closeMenu(true); });
document.addEventListener('click', event => { if (!event.target.closest('.site-header')) closeMenu(); });
window.matchMedia('(min-width: 1024px)').addEventListener('change', event => { if (event.matches) closeMenu(); });

// Semântica e Escape nativos, com ciclo explícito de Tab dentro do modal.
const previousFocus = new WeakMap();
const dialogs = [...document.querySelectorAll('dialog')];
function openDialog(dialog, trigger) {
  closeMenu();
  previousFocus.set(dialog, trigger);
  dialog.showModal();
}
document.addEventListener('keydown', event => {
  if (event.key !== 'Tab' || event.defaultPrevented) return;
  const dialog = dialogs.findLast(item => item.open && item.matches(':modal'));
  if (!dialog) return;
  const focusable = [...dialog.querySelectorAll('a[href], area[href], button, input, select, textarea, summary, iframe, [tabindex], [contenteditable]:not([contenteditable="false"])')].filter(element => {
    const style = getComputedStyle(element);
    return element.tabIndex >= 0 && !element.matches(':disabled, [aria-disabled="true"]') && !element.closest('[hidden], [inert]') && element.getClientRects().length > 0 && style.visibility === 'visible';
  });
  const first = focusable[0];
  const last = focusable.at(-1);
  const active = document.activeElement;
  if (!first) {
    event.preventDefault();
    dialog.focus({ preventScroll: true });
  } else if (!focusable.includes(active) || (event.shiftKey ? active === first : active === last)) {
    event.preventDefault();
    (event.shiftKey ? last : first).focus({ preventScroll: true });
  }
});
for (const dialog of dialogs) {
  dialog.querySelectorAll('[data-close]').forEach(button => button.addEventListener('click', () => dialog.close()));
  dialog.addEventListener('close', () => {
    // `close` é enfileirado: a mesma janela já pode ter sido reaberta.
    if (dialog.open) return;
    const trigger = previousFocus.get(dialog);
    const active = document.activeElement;
    const anotherModal = dialogs.some(item => item !== dialog && item.open && item.matches(':modal'));
    const mayRestore = !anotherModal && (active === document.body || active === document.documentElement || active === trigger || dialog.contains(active));
    // Um acionador do menu pode estar oculto depois do fechamento.
    // Não sobrescrever um foco que o usuário já moveu depois de fechar.
    if (mayRestore) {
      if (trigger?.closest('#mobile-menu')) menuToggle.focus({ preventScroll: true });
      else trigger?.focus({ preventScroll: true });
    }
    if (dialog.id === 'gallery-dialog') document.querySelector('#gallery-image').removeAttribute('src');
  });
  dialog.addEventListener('click', event => {
    if (event.target !== dialog) return;
    const rect = dialog.getBoundingClientRect();
    if (event.clientX < rect.left || event.clientX > rect.right || event.clientY < rect.top || event.clientY > rect.bottom) dialog.close();
  });
}
document.querySelectorAll('[data-pending]').forEach(button => button.addEventListener('click', () => {
  document.querySelector('#pending-title').textContent = button.dataset.pendingTitle || 'Conteúdo em preparação';
  document.querySelector('#pending-message').textContent = button.dataset.pendingMessage || 'Este conteúdo depende de informações e autorização da Fast Limp antes de ser publicado.';
  openDialog(document.querySelector('#pending-dialog'), button);
}));
document.querySelectorAll('[data-gallery]').forEach(button => button.addEventListener('click', () => {
  const image = document.querySelector('#gallery-image');
  image.src = button.dataset.full;
  image.alt = button.querySelector('img')?.alt || 'Limpeza de vidros';
  document.querySelector('#gallery-caption').textContent = button.dataset.caption || image.alt;
  openDialog(document.querySelector('#gallery-dialog'), button);
}));

for (const carousel of document.querySelectorAll('[data-carousel]')) {
  const track = carousel.querySelector('[data-track]');
  const prev = carousel.querySelector('[data-prev]');
  const next = carousel.querySelector('[data-next]');
  if (!track || !prev || !next) continue;
  const cards = [...track.querySelectorAll('.service-card')];
  const choices = [...carousel.querySelectorAll('[data-service-index]')];
  const positionLabel = carousel.querySelector('[data-carousel-position]');
  const update = () => {
    const max = Math.max(0, track.scrollWidth - track.clientWidth);
    const position = Math.max(0, track.scrollLeft);
    prev.disabled = position <= 2;
    next.disabled = position >= max - 2;
    const firstLeft = cards[0]?.offsetLeft || 0;
    const active = position >= max - 2 && max > 0 ? cards.length - 1 : cards.reduce((nearest, card, index) => Math.abs(card.offsetLeft - firstLeft - position) < Math.abs(cards[nearest].offsetLeft - firstLeft - position) ? index : nearest, 0);
    choices.forEach(choice => choice.setAttribute('aria-pressed', String(Number(choice.dataset.serviceIndex) === active)));
    const label = `${active + 1} de ${cards.length} · ${cards[active]?.querySelector('h3')?.textContent || ''}`;
    if (positionLabel && positionLabel.textContent !== label) positionLabel.textContent = label;
  };
  choices.forEach(choice => choice.addEventListener('click', () => {
    const card = cards[Number(choice.dataset.serviceIndex)];
    if (card) track.scrollTo({ left: card.offsetLeft - cards[0].offsetLeft, behavior: motion.matches ? 'instant' : 'smooth' });
  }));
  const scroll = direction => {
    const gap = parseFloat(getComputedStyle(track).gap) || 24;
    const step = (track.firstElementChild?.getBoundingClientRect().width || track.clientWidth) + gap;
    track.scrollBy({ left: direction * step, behavior: motion.matches ? 'instant' : 'smooth' });
  };
  prev.addEventListener('click', () => scroll(-1));
  next.addEventListener('click', () => scroll(1));
  track.addEventListener('scroll', update, { passive: true });
  track.addEventListener('keydown', event => {
    // Não capturar setas em botões/links internos.
    if (event.target !== track || !['ArrowLeft','ArrowRight','Home','End'].includes(event.key)) return;
    event.preventDefault();
    if (event.key === 'ArrowLeft') scroll(-1);
    else if (event.key === 'ArrowRight') scroll(1);
    else track.scrollTo({ left: event.key === 'Home' ? 0 : track.scrollWidth, behavior: motion.matches ? 'instant' : 'smooth' });
  });
  new ResizeObserver(update).observe(track);
  update();
}

const questions = [...document.querySelectorAll('[data-accordion]')];
questions.forEach(question => question.addEventListener('click', () => {
  const opening = question.getAttribute('aria-expanded') !== 'true';
  questions.forEach(item => {
    const expanded = item === question && opening;
    item.setAttribute('aria-expanded', String(expanded));
    const panel = document.getElementById(item.getAttribute('aria-controls'));
    if (panel) panel.hidden = !expanded;
    item.closest('.faq-item')?.classList.toggle('is-open', expanded);
  });
}));
document.querySelectorAll('[data-year]').forEach(element => { element.textContent = new Date().getFullYear(); });
