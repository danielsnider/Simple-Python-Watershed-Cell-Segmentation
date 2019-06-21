#!/usr/bin/env python

import numpy as np
import pylab
import mahotas as mh

def segment_nuc(im):
  T = mh.thresholding.otsu(im) # calculate a threshold value

  # Apply a gaussian filter to smooth the image
  smoothed = mh.gaussian_filter(im, 8)
  thresholded= smoothed > T # do threshold

  # Watershed
  smoothed = mh.gaussian_filter(im, 10)
  regional_max = mh.regmax(smoothed)
  dist_im = mh.distance(thresholded)
  seeds,count = mh.label(regional_max) # nuclei count
  watershedded = mh.cwatershed(dist_im, seeds)

  # Remove areas that aren't nuclei
  watershedded[np.logical_not(thresholded)] = 0


  cell_id = ['abc', 'def', 'ghi']
  # cell_centroid = [(1,2),(3,4)]
  # return watershedded, cell_id
  return watershedded
