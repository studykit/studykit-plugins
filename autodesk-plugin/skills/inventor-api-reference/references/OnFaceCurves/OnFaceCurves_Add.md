# OnFaceCurves.Add Method

Parent Object: [OnFaceCurves](../OnFaceCurves/OnFaceCurves.md)

## Description

Creates a new on face curve.

## Syntax

OnFaceCurves.**Add**( ***Faces*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***FitPoints*** As [NameValueMap](../NameValueMap/NameValueMap.md) ) As [OnFaceCurve](../OnFaceCurve/OnFaceCurve.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Faces | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap object that specifies an array of faces to create the splines on. The faces are in sequence and a face should be connected with the faces that are before and after it in the sequence, otherwise an error will occur. The format is as below: Name = “Face1”. Value = A Face object. The number in the Name is 1-based, and can be increased for more faces to be added. |
| FitPoints | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap object that contains an array of ObjectCollection objects that each ObjectCollection specifies the fit points for a spline curve on a face. The format is as below: Name = “Face1”. Value = An ObjectCollection object that contains the Point or SketchPoint3D objects which indicate the fit points positions. The number in the Name is 1-based and can be increased for more ObjectCollection objects to be added. The name in this argument should be matched to the name in the Faces argument so the fit points are located on the corresponding Face object. If the count of items in this argument is different from that in the Faces argument or the Name are not matched in the Faces and FitPoints argument, an error occurs. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [OnFaceCurve creation](../../sample-programs/OnFaceCurveSample_Sample.md) | This sample demonstrates how to create a OnFaceCurve in 3D sketch. |

## Version

Introduced in version 2017
