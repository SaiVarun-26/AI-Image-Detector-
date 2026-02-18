def ensemble_score(cnn, fft, noise, metadata_flag):
    return 0.4 * cnn + 0.3 * fft + 0.2 * noise + 0.1 * metadata_flag
