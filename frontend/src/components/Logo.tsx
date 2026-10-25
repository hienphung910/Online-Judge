// Logo CodeHub: chu C ghep tu 7 o vuong (cot, hang), o do o giua la "hub".
// Cung hinh voi public/favicon.svg.
const CELLS = [[0, 0], [1, 0], [2, 0], [0, 1], [0, 2], [1, 2], [2, 2]];

export default function Logo({ size }: { size: number }) {
  return (
    <svg width={size} height={size} viewBox="0 0 30 30">
      {CELLS.map(([c, r]) => (
        <rect key={`${c}-${r}`} x={c * 10.5} y={r * 10.5} width="9" height="9" rx="2" fill="#212121" />
      ))}
      <rect x="10.5" y="10.5" width="9" height="9" rx="2" fill="var(--color-red)" />
    </svg>
  );
}
