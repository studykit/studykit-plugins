# SketchImage Object

## Description

The SketchImage object represents an image within a sketch.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../SketchImage/SketchImage_Delete.md) | Method that deletes this object. |
| [GetReferenceKey](../SketchImage/SketchImage_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [MirrorHorizontal](../SketchImage/SketchImage_MirrorHorizontal.md) | Method that mirrors the image horizontally. |
| [MirrorVertical](../SketchImage/SketchImage_MirrorVertical.md) | Method that mirrors the image vertically. |
| [RotateLeft](../SketchImage/SketchImage_RotateLeft.md) | Method that rotates the image counter-clockwise by 90 degrees. |
| [RotateRight](../SketchImage/SketchImage_RotateRight.md) | Method that rotates the image clockwise by 90 degrees. |
| [Update](../SketchImage/SketchImage_Update.md) | Method that updates this image if the linked source file has been modified. This method returns a failure if there is no linked file associated with this image. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../SketchImage/SketchImage_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../SketchImage/SketchImage_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [BoundaryGeometry](../SketchImage/SketchImage_BoundaryGeometry.md) | Property that returns the four construction sketch lines that form the boundary of the image. |
| [ContainingSketchBlock](../SketchImage/SketchImage_ContainingSketchBlock.md) | Property that returns the sketch block that contains this object. This is the same SketchBlock returned as the last item in the SketchBlockPath property. This property returns Nothing if this object does not belong to a sketch block and lives directly under a sketch. |
| [Height](../SketchImage/SketchImage_Height.md) | Get and set the image height. |
| [Image](../SketchImage/SketchImage_Image.md) | Gets the Picture object representing the associated bitmap. |
| [ImageAlpha](../SketchImage/SketchImage_ImageAlpha.md) | Gets the Alpha channel bitmap of the Picture object representing the associated bitmap. Returns Nothing if there is no alpha data being used. |
| [LinkedToFile](../SketchImage/SketchImage_LinkedToFile.md) | Property that returns whether this image is linked to the picture file that was used to create this image. |
| [Name](../SketchImage/SketchImage_Name.md) | Gets and sets the name of the image. |
| [Parent](../SketchImage/SketchImage_Parent.md) | Property that returns the parent sketch. |
| [Position](../SketchImage/SketchImage_Position.md) | Gets and sets the position of the image on the sketch. |
| [ReferencedFileDescriptor](../SketchImage/SketchImage_ReferencedFileDescriptor.md) | Property that returns the reference to the picture file used to create this image. This property returns Nothing if the source file is not linked (use the LinkedToFile property to determine this). |
| [SketchBlockPath](../SketchImage/SketchImage_SketchBlockPath.md) | Property that returns the path of sketch blocks at the leaf of which this sketch object is found. The enumerator returns a count of 0 if the object lives directly under a sketch. |
| [Transparent](../SketchImage/SketchImage_Transparent.md) | Gets and sets whether the image is transparent. |
| [Type](../SketchImage/SketchImage_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Visible](../SketchImage/SketchImage_Visible.md) | Gets and sets whether the image is visible. |
| [Width](../SketchImage/SketchImage_Width.md) | Get and set the image width. |

## Accessed From

[DecalFeature.Image](../DecalFeature/DecalFeature_Image.md), [DecalFeatureProxy.Image](../DecalFeatureProxy/DecalFeatureProxy_Image.md), [SketchImageProxy.NativeObject](../SketchImageProxy/SketchImageProxy_NativeObject.md), [SketchImages.Add](../SketchImages/SketchImages_Add.md), [SketchImages.Item](../SketchImages/SketchImages_Item.md)

## Derived Classes

[SketchImageProxy](../SketchImageProxy/SketchImageProxy.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Add a decal feature](../../sample-programs/DecalFeatures_Add_Sample.md) | This sample demonstrates the creation of a decal feature. |

## Version

Introduced in version 11
