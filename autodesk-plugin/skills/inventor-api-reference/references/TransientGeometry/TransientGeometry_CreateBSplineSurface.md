# TransientGeometry.CreateBSplineSurface Method

Parent Object: [TransientGeometry](../TransientGeometry/TransientGeometry.md)

## Description

Method that creates a new BSplineSurface object. The definition of the surface is supplied using the input \arguments. If an invalid surface is defined the method will fail. The object created is a transient mathematical object and is not displayed graphically.

## Syntax

TransientGeometry.**CreateBSplineSurface**( ***Order***() As Long, ***Poles***() As Double, ***KnotsU***() As Double, ***KnotsV***() As Double, ***Weights***() As Double, ***IsPeriodic***() As Boolean ) As [BSplineSurface](../BSplineSurface/BSplineSurface.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Order | Long | Input array of Longs that specifies the order of the surface in the U and V directions. The size of this array should be 2. |
| Poles | Double | Input array of Doubles that contains the coordinates of the surface. The array contains X, Y, Z coordinates of each pole. The first row of poles along the U direction are specified, then stepping in the V direction the next row of poles along the U direction are specified. The size of this array should be U Pole Count \* V Pole Count \* 3. |
| KnotsU | Double | Input array of Doubles that contains the knot vectors along the U direction of the surface. |
| KnotsV | Double | Input array of Doubles that contains the knot vectors along the V direction of the surface. |
| Weights | Double | Input array of Doubles that contains the weight factor for each pole for a rational surface. The weights for the first row of poles along the U direction are specified, then stepping in the V direction the weights for the next row of poles along the U direction are specified. |
| IsPeriodic | Boolean | Input array of Booleans that specifies if the surface is periodic in the U and V directions. True if it is periodic False if it is non\-periodic. The size of this array should be 2. |

## Version

Introduced in version 4
