// Fallback node algorithm (js)
for (let i = 1; i < N; i++) {
  const childStatus = tick(children[i]);
  if (childStatus === 'Running') {
    return 'Running';
  } else if (childStatus === 'Success') {
    return 'Failure';
  }
}
return 'Failure';
