// Parallel node algorithm (js)
const childrenStatus = [];
for (let i = 1; i < N; i++) {
  childrenStatus.push(tick(children[i]));
}
if (childrenStatus.filter((status) => status === 'Success').length >= M) {
  return 'Success';
} else if (
  childrenStatus.filter((status) => status === 'Failure').length >
  N - M
) {
  return 'Failure';
}
return 'Running';
