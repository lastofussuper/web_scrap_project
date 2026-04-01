/**
* extract_item_urls.js
*
*Browser console script
*usage:
*1.open second-hand platform hidden items page (username password login required)
*2.scroll to load all items
*3.Open devtools console (right click-->inspect--> and u will see console on edge browser)
*use below scripts

console.clear()

const links = Array.from(
  document.querySelectorAll('a[href*="/items/"]')
);

const rows = links
  .map(a => a.href.split("?")[0])
  .filter(url => /\/items\/\d+/.test(url))
  .map(url => ({ url }));

const uniqueRows = Array.from(
  new Map(rows.map(r => [r.url, r])).values()
);

console.log(JSON.stringify(uniqueRows, null, 2));



