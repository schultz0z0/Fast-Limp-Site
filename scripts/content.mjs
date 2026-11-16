const title = 'Fast Limp — Limpeza de vidros no Rio de Janeiro';
const description = 'Limpeza de vidros residenciais, comerciais, pós-obra, fachadas e vitrines no Rio de Janeiro. Peça um orçamento à Fast Limp pelo WhatsApp.';

function publicMetadata(content) {
  const image = new URL('assets/brand/fast-limp-social.jpg', content.siteUrl);
  const imageAlt = 'Fast Limp — Limpeza de vidros no Rio de Janeiro';
  const business = {
    '@context': 'https://schema.org',
    '@type': 'LocalBusiness',
    '@id': new URL('#fast-limp', content.siteUrl),
    name: 'Fast Limp',
    url: content.siteUrl,
    description,
    logo: new URL('assets/brand/fast-limp-simbolo-principal.svg', content.siteUrl),
    image,
    telephone: `+${content.phone}`,
    keywords: ['limpeza de vidros'],
    contactPoint: {
      '@type': 'ContactPoint',
      contactType: 'Orçamentos e atendimento',
      telephone: `+${content.phone}`,
      url: new URL('contact', content.siteUrl),
      availableLanguage: 'pt-BR',
    },
    areaServed: { '@type': 'City', name: content.region },
    hasOfferCatalog: {
      '@type': 'OfferCatalog',
      name: 'Limpeza de vidros',
      itemListElement: content.services.map(name => ({
        '@type': 'Offer',
        itemOffered: { '@type': 'Service', name, serviceType: 'Limpeza de vidros' },
      })),
    },
  };
  return `<link rel="canonical" href="${content.siteUrl}">
  <link rel="alternate" type="text/markdown" href="${new URL('index.md', content.siteUrl)}">
  <link rel="describedby" href="${new URL('llms.txt', content.siteUrl)}">
  <meta property="og:type" content="website">
  <meta property="og:locale" content="pt_BR">
  <meta property="og:site_name" content="Fast Limp">
  <meta property="og:url" content="${content.siteUrl}">
  <meta property="og:title" content="${title}">
  <meta property="og:description" content="${description}">
  <meta property="og:image" content="${image}">
  <meta property="og:image:type" content="image/jpeg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="${imageAlt}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="${title}">
  <meta name="twitter:description" content="${description}">
  <meta name="twitter:image" content="${image}">
  <meta name="twitter:image:alt" content="${imageAlt}">
  <script type="application/ld+json">${JSON.stringify(business).replaceAll('<', '\\u003c')}</script>`;
}

export function whatsappUrl(phone, context = '') {
  if (!/^55\d{10,11}$/.test(phone)) throw new Error('WhatsApp deve incluir país e DDD, somente dígitos');
  const message = context
    ? `Olá, Fast Limp! Gostaria de solicitar informações sobre ${context}. Meu bairro no Rio de Janeiro é: `
    : 'Olá, Fast Limp! Gostaria de solicitar um orçamento para limpeza de vidros. Meu bairro no Rio de Janeiro é: ';
  return `https://wa.me/${phone}?text=${encodeURIComponent(message)}`;
}

export function renderContent(html, content, production = false) {
  const starts = (html.match(/<!-- PREVIEW-ONLY:START -->/g) || []).length;
  const ends = (html.match(/<!-- PREVIEW-ONLY:END -->/g) || []).length;
  if (starts !== ends) throw new Error('Blocos de demonstração sem fechamento');
  if (production) html = html.replace(/<!-- PREVIEW-ONLY:START -->[\s\S]*?<!-- PREVIEW-ONLY:END -->/g, '');
  html = html
    .replace('<!-- PUBLIC-PAGES -->', production ? '<nav aria-label="Informações da empresa"><a href="/about">Sobre</a> · <a href="/contact">Contato</a> · <a href="/privacy">Privacidade</a></nav>' : '')
    .replace('{{TITLE}}', title)
    .replace('{{DESCRIPTION}}', description)
    .replace('<!-- INDEXING -->', () => production ? publicMetadata(content) : '<meta name="robots" content="noindex, nofollow">');
  html = html.replace(/<button\b([^>]*\bdata-contact\b[^>]*)>([\s\S]*?)<\/button>/g, (_, attributes, label) => {
    const context = attributes.match(/data-context="([^"]*)"/)?.[1] || '';
    const url = whatsappUrl(content.phone, context).replaceAll('&', '&amp;');
    return `<a${attributes.replace(/\s*type="button"/g, '')} href="${url}" target="_blank" rel="noopener noreferrer">${label}</a>`;
  });
  for (const [key, value] of Object.entries({ PHONE_DISPLAY: content.phoneDisplay, REGION: content.region })) html = html.replaceAll(`{{${key}}}`, value);
  return html.replace('data-content-mode="local-review"', `data-content-mode="${production ? 'production' : 'local-review'}"`);
}
