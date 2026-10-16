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
  html = html.replace(/<button\b([^>]*\bdata-contact\b[^>]*)>([\s\S]*?)<\/button>/g, (_, attributes, label) => {
    const context = attributes.match(/data-context="([^"]*)"/)?.[1] || '';
    const url = whatsappUrl(content.phone, context).replaceAll('&', '&amp;');
    return `<a${attributes.replace(/\s*type="button"/g, '')} href="${url}" target="_blank" rel="noopener noreferrer">${label}</a>`;
  });
  for (const [key, value] of Object.entries({ PHONE_DISPLAY: content.phoneDisplay, REGION: content.region })) html = html.replaceAll(`{{${key}}}`, value);
  return html.replace('data-content-mode="local-review"', `data-content-mode="${production ? 'production' : 'local-review'}"`);
}
