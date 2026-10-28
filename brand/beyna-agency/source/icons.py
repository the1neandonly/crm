"""Beyna service icons — 48u grid, solid geometry, one lime accent per icon (echoes the slice)."""
def ring(cx, cy, r1, r2): return f'M{cx-r1},{cy}a{r1},{r1} 0 1,0 {2*r1},0a{r1},{r1} 0 1,0 {-2*r1},0Z M{cx-r2},{cy}a{r2},{r2} 0 1,1 {2*r2},0a{r2},{r2} 0 1,1 {-2*r2},0Z'
ICONS = {
 'strategy': lambda c, a: f'<path fill-rule="evenodd" fill="{c}" d="{ring(24,24,20,13)}"/><circle cx="24" cy="24" r="6.5" fill="{a}"/>',
 'branding': lambda c, a: f'<rect x="5" y="5" width="24" height="24" rx="4" fill="{c}"/><path d="M43,43 H22 A21,21 0 0,1 43,22 Z" fill="{a}"/>',
 'social':   lambda c, a: f'<path fill="{c}" d="M13,7 H35 A8,8 0 0,1 43,15 V29 A8,8 0 0,1 35,37 H17 L7,44 V15 A8,8 0 0,1 13,7Z"/><circle cx="17" cy="22" r="3" fill="{a}"/><circle cx="25" cy="22" r="3" fill="{a}"/><circle cx="33" cy="22" r="3" fill="{a}"/>',
 'ads':      lambda c, a: f'<path fill="{c}" d="M6,17 H14 L32,7 V41 L14,31 H6 A2,2 0 0,1 4,29 V19 A2,2 0 0,1 6,17Z"/><rect x="11" y="31" width="7" height="11" rx="2" fill="{c}"/><path d="M36,15 A12,12 0 0,1 36,33 Z" fill="{a}"/>',
 'video':    lambda c, a: f'<rect x="4" y="9" width="40" height="30" rx="7" fill="{c}"/><path d="M20,16.5 L32,24 L20,31.5Z" fill="{a}"/>',
 'web':      lambda c, a: f'<path fill-rule="evenodd" fill="{c}" d="M9,7 H39 A5,5 0 0,1 44,12 V36 A5,5 0 0,1 39,41 H9 A5,5 0 0,1 4,36 V12 A5,5 0 0,1 9,7Z M9,18 V36 H39 V18Z"/><circle cx="10.5" cy="12.5" r="2" fill="{a}"/><circle cx="16.5" cy="12.5" r="2" fill="{a}"/><path d="M24,36 V25 A11,11 0 0,1 35,36Z" fill="{a}"/>',
 'analytics':lambda c, a: f'<rect x="5" y="26" width="9" height="17" rx="2.5" fill="{c}"/><rect x="19.5" y="16" width="9" height="27" rx="2.5" fill="{c}"/><rect x="34" y="5" width="9" height="38" rx="2.5" fill="{a}"/>',
 'events':   lambda c, a: f'<path fill-rule="evenodd" fill="{c}" d="M10,9 H38 A5,5 0 0,1 43,14 V38 A5,5 0 0,1 38,43 H10 A5,5 0 0,1 5,38 V14 A5,5 0 0,1 10,9Z M10,19 V38 H38 V19Z"/><rect x="14" y="4" width="5" height="9" rx="2" fill="{c}"/><rect x="29" y="4" width="5" height="9" rx="2" fill="{c}"/><rect x="27" y="25" width="8" height="8" rx="2" fill="{a}"/>',
 'email':    lambda c, a: f'<rect x="4" y="9" width="40" height="30" rx="6" fill="{c}"/><path d="M9,15 L24,26 L39,15" fill="none" stroke="{a}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>',
 'search':   lambda c, a: f'<path fill-rule="evenodd" fill="{c}" d="{ring(20,20,15,8.5)}"/><rect x="29" y="27" width="8" height="18" rx="3" transform="rotate(-45 33 36)" fill="{a}"/>',
 'photo':    lambda c, a: f'<rect x="4" y="13" width="40" height="28" rx="6" fill="{c}"/><rect x="15" y="7" width="18" height="10" rx="3" fill="{c}"/><circle cx="24" cy="27" r="8" fill="{a}"/>',
 'growth':   lambda c, a: f'<path fill="{c}" d="M4,24 H24 V4 A20,20 0 1,1 4,24Z"/><path d="M20,20 H8 A12,12 0 0,1 20,8Z" fill="{a}"/>',
 'team':     lambda c, a: f'<circle cx="17" cy="15" r="8" fill="{c}"/><path d="M3,42 A14,14 0 0,1 31,42Z" fill="{c}"/><circle cx="34" cy="17" r="6" fill="{a}"/><path d="M33,42 A12,12 0 0,0 26,30.5 A11,11 0 0,1 45,42Z" fill="{a}"/>',
 'contact':  lambda c, a: f'<path fill="{c}" d="M11,5 L19,5 L22,15 L17,19 A24,24 0 0,0 29,31 L33,26 L43,29 L43,37 A6,6 0 0,1 37,43 A32,32 0 0,1 5,11 A6,6 0 0,1 11,5Z"/><path d="M28,5 A15,15 0 0,1 43,20 H37 A9,9 0 0,0 28,11Z" fill="{a}"/>',
 'star':     lambda c, a: f'<path fill="{c}" d="M24,4 L29.5,17.5 L44,18.5 L33,28 L36.5,42.5 L24,34.5 L11.5,42.5 L15,28 L4,18.5 L18.5,17.5Z"/><circle cx="24" cy="24" r="5" fill="{a}"/>',
 'idea':     lambda c, a: f'<path fill="{c}" d="M24,4 A15,15 0 0,1 33,31 V35 H15 V31 A15,15 0 0,1 24,4Z"/><rect x="16" y="38" width="16" height="6" rx="3" fill="{a}"/>',
}
def icon_svg(name, c, a, size=None):
    sz = f' width="{size}" height="{size}"' if size else ''
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"{sz}>{ICONS[name](c, a)}</svg>'
