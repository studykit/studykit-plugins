# Color Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Application/Color.h>

## Description

The Color class wraps all of the information that defines a simple color.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](Color_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [create](Color_create.htm) | Creates a new color. |
| [getColor](Color_getColor.htm) | Gets all of the information defining this color. |
| [setColor](Color_setColor.htm) | Sets all of the color information. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [blue](Color_blue.htm) | Gets and sets the blue component of the color. The value can be 0 to 255. |
| [green](Color_green.htm) | Gets and sets the green component of the color. The value can be 0 to 255. |
| [isValid](Color_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](Color_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [opacity](Color_opacity.htm) | Gets and sets the opacity of the color. The value can be 0 to 255. A value of 0 is transparent and 255 is opaque. |
| [red](Color_red.htm) | Gets and sets the red component of the color. The value can be 0 to 255. |

## Accessed From

[Color.create](Color_create.htm), [ColorControlPoint.value](ColorControlPoint_value.htm), [ColorGraphNodeProperty.value](ColorGraphNodeProperty_value.htm), [ColorProperty.value](ColorProperty_value.htm), [ColorProperty.values](ColorProperty_values.htm), [Component.componentColor](Component_componentColor.htm), [CustomGraphicsBasicMaterialColorEffect.ambientColor](CustomGraphicsBasicMaterialColorEffect_ambientColor.htm), [CustomGraphicsBasicMaterialColorEffect.diffuseColor](CustomGraphicsBasicMaterialColorEffect_diffuseColor.htm), [CustomGraphicsBasicMaterialColorEffect.emissiveColor](CustomGraphicsBasicMaterialColorEffect_emissiveColor.htm), [CustomGraphicsBasicMaterialColorEffect.specularColor](CustomGraphicsBasicMaterialColorEffect_specularColor.htm), [CustomGraphicsCoordinates.getColor](CustomGraphicsCoordinates_getColor.htm), [CustomGraphicsShowThroughColorEffect.color](CustomGraphicsShowThroughColorEffect_color.htm), [CustomGraphicsSolidColorEffect.color](CustomGraphicsSolidColorEffect_color.htm), [FlatPatternComponent.componentColor](FlatPatternComponent_componentColor.htm), [SceneSettings.backgroundSolidColor](SceneSettings_backgroundSolidColor.htm), [SectionAnalysis.sectionColor](SectionAnalysis_sectionColor.htm), [SectionAnalysisInput.sectionColor](SectionAnalysisInput_sectionColor.htm), [VolumetricColorSample.value](VolumetricColorSample_value.htm)

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |