# SketchImageProxy Object

Derived from: [SketchImage](../SketchImage/SketchImage.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../SketchImageProxy/SketchImageProxy_Delete.md) | Method that deletes this object. |
| [GetReferenceKey](../SketchImageProxy/SketchImageProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [MirrorHorizontal](../SketchImageProxy/SketchImageProxy_MirrorHorizontal.md) | Method that mirrors the image horizontally. |
| [MirrorVertical](../SketchImageProxy/SketchImageProxy_MirrorVertical.md) | Method that mirrors the image vertically. |
| [RotateLeft](../SketchImageProxy/SketchImageProxy_RotateLeft.md) | Method that rotates the image counter-clockwise by 90 degrees. |
| [RotateRight](../SketchImageProxy/SketchImageProxy_RotateRight.md) | Method that rotates the image clockwise by 90 degrees. |
| [Update](../SketchImageProxy/SketchImageProxy_Update.md) | Method that updates this image if the linked source file has been modified. This method returns a failure if there is no linked file associated with this image. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../SketchImageProxy/SketchImageProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../SketchImageProxy/SketchImageProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [BoundaryGeometry](../SketchImageProxy/SketchImageProxy_BoundaryGeometry.md) | Property that returns the four construction sketch lines that form the boundary of the image. |
| [ContainingOccurrence](../SketchImageProxy/SketchImageProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [ContainingSketchBlock](../SketchImageProxy/SketchImageProxy_ContainingSketchBlock.md) | Property that returns the sketch block that contains this object. This is the same SketchBlock returned as the last item in the SketchBlockPath property. This property returns Nothing if this object does not belong to a sketch block and lives directly under a sketch. |
| [Height](../SketchImageProxy/SketchImageProxy_Height.md) | Get and set the image height. |
| [Image](../SketchImageProxy/SketchImageProxy_Image.md) | Gets the Picture object representing the associated bitmap. |
| [ImageAlpha](../SketchImageProxy/SketchImageProxy_ImageAlpha.md) | Gets the Alpha channel bitmap of the Picture object representing the associated bitmap. Returns Nothing if there is no alpha data being used. |
| [LinkedToFile](../SketchImageProxy/SketchImageProxy_LinkedToFile.md) | Property that returns whether this image is linked to the picture file that was used to create this image. |
| [Name](../SketchImageProxy/SketchImageProxy_Name.md) | Gets and sets the name of the image. |
| [NativeObject](../SketchImageProxy/SketchImageProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [Parent](../SketchImageProxy/SketchImageProxy_Parent.md) | Property that returns the parent sketch. |
| [Position](../SketchImageProxy/SketchImageProxy_Position.md) | Gets and sets the position of the image on the sketch. |
| [ReferencedFileDescriptor](../SketchImageProxy/SketchImageProxy_ReferencedFileDescriptor.md) | Property that returns the reference to the picture file used to create this image. This property returns Nothing if the source file is not linked (use the LinkedToFile property to determine this). |
| [SketchBlockPath](../SketchImageProxy/SketchImageProxy_SketchBlockPath.md) | Property that returns the path of sketch blocks at the leaf of which this sketch object is found. The enumerator returns a count of 0 if the object lives directly under a sketch. |
| [Transparent](../SketchImageProxy/SketchImageProxy_Transparent.md) | Gets and sets whether the image is transparent. |
| [Type](../SketchImageProxy/SketchImageProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Visible](../SketchImageProxy/SketchImageProxy_Visible.md) | Gets and sets whether the image is visible. |
| [Width](../SketchImageProxy/SketchImageProxy_Width.md) | Get and set the image width. |

## Version

Introduced in version 11
