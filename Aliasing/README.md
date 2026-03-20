# Aliasing

Aliasing is a distortion that occurs when a signal is sampled at a lower rate than the original image.
After reconstructing signal from samples of the original singal it contains low-frequency components that are not present in the original one.


There are some methods to prevent aliasing effect: sampling the signal correctly,
using anti-aliasing filters (filters which can prevent or block any frequencies higher than a specific limit) or
oversampling (a technique to measure the signal at a much higher rate than actually needed).
