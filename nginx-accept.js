function preference(ranges, subtype) {
    let result = { quality: 0, specificity: -1 };

    for (let index = 0; index < ranges.length; index++) {
        const parts = ranges[index].trim().toLowerCase()
            .split(/;(?=(?:[^"]*"[^"]*")*[^"]*$)/);
        const type = parts[0].trim();
        let specificity = type === `text/${subtype}` ? 2 : type === 'text/*' ? 1 : type === '*/*' ? 0 : -1;
        if (specificity < 0) continue;

        let quality = 1;
        let accepted = true;
        for (let index = 1; index < parts.length; index++) {
            const pair = parts[index].trim().split(/\s*=\s*/, 2);
            const name = pair[0];
            const value = pair[1];
            if (name === 'q') {
                quality = /^(?:0(?:\.\d{0,3})?|1(?:\.0{0,3})?)$/.test(value) ? Number(value) : 0;
                break;
            }
            if (name !== 'charset' || !/^(?:utf-8|"utf-8")$/.test(value)) {
                accepted = false;
                break;
            }
            specificity += 3;
        }
        if (accepted && (specificity > result.specificity ||
            (specificity === result.specificity && quality > result.quality))) {
            result = { quality, specificity };
        }
    }

    return result;
}

function representation(request) {
    const accept = request.headersIn.Accept;
    if (accept === undefined) return 'html';
    const ranges = accept.split(/,(?=(?:[^"]*"[^"]*")*[^"]*$)/);
    const html = preference(ranges, 'html');
    const markdown = preference(ranges, 'markdown');

    if (html.quality === 0 && markdown.quality === 0) return 'unacceptable';
    if (markdown.quality > html.quality ||
        (markdown.quality === html.quality && markdown.specificity > html.specificity)) return 'markdown';
    return 'html';
}

export default { representation };
