# Materials Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Materials/Materials.h>

## Description

Collection of materials within a Library or Design.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [addByCopy](Materials_addByCopy.htm) | Add a Material to a Design by copying an existing Material from Favorites, a Library or from the Materials stored in the Design. This method currently only applies to the Materials collection from a Design and cannot be used to copy a Material to a library. |
| [classType](Materials_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](Materials_item.htm) | Returns the specified Material using an index into the collection. |
| [itemById](Materials_itemById.htm) | Returns the Material by it's internal unique ID. |
| [itemByName](Materials_itemByName.htm) | Returns the specified Material using the name as seen in the user interface. This often isn't a reliable way of accessing a specific material because materials are not required to be unique. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](Materials_count.htm) | The number of Materials in the collection. |
| [isValid](Materials_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](Materials_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[Design.materials](Design_materials.htm), [FlatPatternProduct.materials](FlatPatternProduct_materials.htm), [MaterialLibrary.materials](MaterialLibrary_materials.htm), [WorkingModel.materials](WorkingModel_materials.htm)

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |