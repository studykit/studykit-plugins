# LightingStyle Object

## Description

The LightingStyle object provides access to all of the properties that define a specific lighting style.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [ConvertToLocal](../LightingStyle/LightingStyle_ConvertToLocal.md) | Method that creates a local cached copy of a global style and returns the local style. This method fails if this style is already local. Use the StyleLocation property to determine whether the style is local. |
| [Copy](../LightingStyle/LightingStyle_Copy.md) | Method that copies the rendering style and assigns the specified name to the copy. The new style is returned by the method. |
| [Delete](../LightingStyle/LightingStyle_Delete.md) | Method that deletes the LightingStyle. |
| [GetReferenceKey](../LightingStyle/LightingStyle_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [SaveToGlobal](../LightingStyle/LightingStyle_SaveToGlobal.md) | Method that saves this style to the global repository. If a style with the same name is found in the repository, that style is updated. |
| [UpdateFromGlobal](../LightingStyle/LightingStyle_UpdateFromGlobal.md) | Method that updates this style from the global repository. |
| [UploadImage](../LightingStyle/LightingStyle_UploadImage.md) | Upload an IBL image to current lighting style. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Ambience](../LightingStyle/LightingStyle_Ambience.md) | Gets and sets the ambience of the lighting style. |
| [AmbientShadowIntensity](../LightingStyle/LightingStyle_AmbientShadowIntensity.md) | Gets and sets the intensity of the ambient shadow (occlusion). |
| [Application](../LightingStyle/LightingStyle_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../LightingStyle/LightingStyle_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Brightness](../LightingStyle/LightingStyle_Brightness.md) | Gets and sets the brightness of the lighting style. |
| [Exposure](../LightingStyle/LightingStyle_Exposure.md) | Gets and sets the exposure of the lighting style. |
| [ImageBasedLightingBrightness](../LightingStyle/LightingStyle_ImageBasedLightingBrightness.md) | Gets and sets the brightness of the lighting style. |
| [ImageBasedLightingRotation](../LightingStyle/LightingStyle_ImageBasedLightingRotation.md) | Gets and sets the rotation to be applied to the image. |
| [ImageBasedLightingScale](../LightingStyle/LightingStyle_ImageBasedLightingScale.md) | Gets and sets the scale to be applied to the image. |
| [ImageBasedLightingShowImage](../LightingStyle/LightingStyle_ImageBasedLightingShowImage.md) | Gets and sets whether to display the image in the graphics scene. |
| [InternalName](../LightingStyle/LightingStyle_InternalName.md) | property that returns the unique name of the style. The name is the internal English name of the style. This name will remain constant and is not affected by locale. This name is never displayed to the user. |
| [InUse](../LightingStyle/LightingStyle_InUse.md) | Property that indicates if this style is in use. |
| [LightingStyleType](../LightingStyle/LightingStyle_LightingStyleType.md) | Gets the lighting style type. |
| [Lights](../LightingStyle/LightingStyle_Lights.md) | Property that returns the Lights collection object. |
| [Name](../LightingStyle/LightingStyle_Name.md) | Gets and sets the lighting style name. |
| [Parent](../LightingStyle/LightingStyle_Parent.md) | Property returning the parent of the object. |
| [ShadowDensity](../LightingStyle/LightingStyle_ShadowDensity.md) | Gets and sets the direction of the light source that controls the shadow. |
| [ShadowDirection](../LightingStyle/LightingStyle_ShadowDirection.md) | Gets and sets the direction of the light source that controls the shadow. |
| [ShadowSoftness](../LightingStyle/LightingStyle_ShadowSoftness.md) | Gets and sets the blending between shadowed and non-shadowed areas. |
| [StyleLocation](../LightingStyle/LightingStyle_StyleLocation.md) | Property that returns the location of this lighting style, i.e. local to the document, cached locally in the document, exists in the library. Lighting styles that exist in the library cannot be edited. |
| [Type](../LightingStyle/LightingStyle_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UpToDate](../LightingStyle/LightingStyle_UpToDate.md) | Property that gets the up-to-date status of the style against the global repository. |

## Accessed From

[AssemblyDocument.ActiveLightingStyle](../AssemblyDocument/AssemblyDocument_ActiveLightingStyle.md), [Light.Parent](../Light/Light_Parent.md), [LightingStyle.ConvertToLocal](../LightingStyle/LightingStyle_ConvertToLocal.md), [LightingStyle.Copy](../LightingStyle/LightingStyle_Copy.md), [LightingStyles.Add](../LightingStyles/LightingStyles_Add.md), [LightingStyles.Item](../LightingStyles/LightingStyles_Item.md), [PartDocument.ActiveLightingStyle](../PartDocument/PartDocument_ActiveLightingStyle.md), [PresentationDocument.ActiveLightingStyle](../PresentationDocument/PresentationDocument_ActiveLightingStyle.md)

## Version

Introduced in version 10

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |