# Properties Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Application/Properties.h>

## Description

A collection of properties that are associated with a material or appearance.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](Properties_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](Properties_item.htm) | Returns the specified property from the collection using an index into the collection. |
| [itemById](Properties_itemById.htm) | Returns the specified property from the collection using the unique ID of the property. |
| [itemByName](Properties_itemByName.htm) | Returns the specified Property using the name of the property. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](Properties_count.htm) | Returns the number of properties within the collection. |
| [isValid](Properties_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](Properties_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[Appearance.appearanceProperties](Appearance_appearanceProperties.htm), [AppearanceTexture.properties](AppearanceTexture_properties.htm), [Material.materialProperties](Material_materialProperties.htm)

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |