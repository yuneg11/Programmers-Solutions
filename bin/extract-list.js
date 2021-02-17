// Initialize
let list = [];
const exts = {
    'c': 'c','cpp': 'cpp','csharp': 'cs','go': 'go','java': 'java','javascript': 'js',
    'kotlin': 'kt','mysql': 'm.sql','oracle': 'o.sql','python2': '2.py','python3': 'py',
    'ruby': 'rb','scala': 'scala', 'swift': 'swift',
};
const f = () => [...document.querySelectorAll('.algorithm-list > .row  .col-item > .card-algorithm')].map(e => {
    const link = e.children[0].href;
    const id = link.split('/')[7];
    const level = e.className.split(' ')[1].split('-')[1];
    const title = e.children[0].children[0].textContent;
    const category = e.children[0].children[1].children[0].textContent;
    const dir = `/solutions/${id}%20-%20${title.replace(/ /g, '%20')}`;
    const lang = [...e.querySelectorAll('.languages .ic-added-circle')]
                    .map(x => x.parentElement.parentElement.getAttribute('data-original-title'))
                    .map(l => `[![${l}](/assets/${l}.svg)](${dir}/solution.${exts[l]})`).join(' ');
    return `| ${id} | Level ${level} | ${title} | ${category} | [문제](${link}) / [풀이](${dir}) | ${lang} |`;
});

// Per page (please click manually)
list = list.concat(f());

// Finalize
list.sort().join('\n');
