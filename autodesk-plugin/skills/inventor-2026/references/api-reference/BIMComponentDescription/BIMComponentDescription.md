# BIMComponentDescription Object

## Description

BIMComponentDescription object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [SetCustomThumbnail](../BIMComponentDescription/BIMComponentDescription_SetCustomThumbnail.md) | Method that lets you set the custom thumbnail by providing the filename of an image file. The file should be a bmp, jpg, or png format and should be 256x256 pixels. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../BIMComponentDescription/BIMComponentDescription_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [ComponentPropertySets](../BIMComponentDescription/BIMComponentDescription_ComponentPropertySets.md) | Read-only property that returns the collection object containing the property sets for a BIM component. |
| [FamilyType](../BIMComponentDescription/BIMComponentDescription_FamilyType.md) | Read-write property that gets and sets the family type. This is applicable for IFC and RFA formats. |
| [ModelProperties](../BIMComponentDescription/BIMComponentDescription_ModelProperties.md) | Read-write property that gets and sets the standard Inventor iProperties that are exported with this component. |
| [OrientationType](../BIMComponentDescription/BIMComponentDescription_OrientationType.md) | Read-write property that specifies which orientation type will be used when exporting the BIM component. |
| [RevitFamilyCategory](../BIMComponentDescription/BIMComponentDescription_RevitFamilyCategory.md) | Read-write property that gets and sets the Revit family category Id. |
| [Thumbnail](../BIMComponentDescription/BIMComponentDescription_Thumbnail.md) | Read-write property that gets and sets the thumbnail for this component. |
| [Type](../BIMComponentDescription/BIMComponentDescription_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UserCoordinateSystemOrientation](../BIMComponentDescription/BIMComponentDescription_UserCoordinateSystemOrientation.md) | Read-write property that defines which user coordinate system will be used when exporting the component. If the OrientationType is not kUserCoordinateSystemOrientationType this property returns Nothing. |
| [ViewCubeOrientationOrigin](../BIMComponentDescription/BIMComponentDescription_ViewCubeOrientationOrigin.md) | Read-write property that gets and set the origin of the coordinate system when the orientation is defined using the ViewCube. |

## Accessed From

[BIMComponent.ComponentDescription](../BIMComponent/BIMComponent_ComponentDescription.md)

## Version

Introduced in version 2011
