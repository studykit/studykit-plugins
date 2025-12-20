# DecalFeatures.Add Method

Parent Object: [DecalFeatures](../DecalFeatures/DecalFeatures.md)

## Description

Method that creates a new decal feature by applying an image on one or more faces in the model.

## Remarks

If the decal feature is created successfully, a DecalFeature object corresponding to the newly created decal feature is returned from this method.

## Syntax

DecalFeatures.**Add**( ***Image*** As [SketchImage](../SketchImage/SketchImage.md), ***Face*** As [Face](../Face/Face.md), [***WrapFace***] As Boolean, [***ChainFaces***] As Boolean ) As [DecalFeature](../DecalFeature/DecalFeature.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Image | [SketchImage](../SketchImage/SketchImage.md) | Input SketchImage object used to define the sketch image used to apply the decal. |
| Face | [Face](../Face/Face.md) | Input Face object that defines the primary face on which the decal should be applied. The orientation of the face must be such that the image can be projected onto the face, otherwise the creation of the decal will fail. If the face is planar, then the angle between the normal vector of the face and the normal vector of the sketch plane that contains the image should be less than 90 degrees. If this angle is equal to 90 degrees (which means that the plane of the face is perpendicular to the plane of the image) or if this angle is greater than 90 degrees, then the creation of the decal will fail. For example, if the face is planar and the plane of the face is perpendicular to the plane of the image, then the creation of the decal will fail. |
| WrapFace | Boolean | Optional Input Boolean that specifies if the image should be wrapped on the face on which the decal needs to be applied. If a value of True is specified, then the image will be wrapped on the face on which the decal is applied. But, the image will be wrapped on the face only if the face is tangential to the plane of the image. If the face is not tangential to the plane of the image and a value of True is specified for this argument, then the creation of the decal will fail. The effects of wrapping the decal are pronounced if the face is a curved face. If a value of False is specified, then it implies that the decal feature should not be wrapped around the face, but created as a result of straight projection onto the face. A default value of False will be assumed if no value is explicitly specified for this argument. |
| ChainFaces | Boolean | Optional Input Boolean that specifies whether the decal should also be applied on any faces that are adjacent to the primary face on which the decal needs to be applied. If a value of True is specified, then the decal will also be applied on adjacent faces in addition to the primary face specified by the Face argument. If there are no adjacent faces, then the decal will be applied only on the primary face. If a value of False is specified, then the decal will be applied only on the primary face specified by the Face argument. A default value of True will be assumed if no value is explicitly specified for this argument.   This is an optional argument whose default value is True. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Add a decal feature](../../sample-programs/DecalFeatures_Add_Sample.md) | This sample demonstrates the creation of a decal feature. |

## Version

Introduced in version 2008

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |