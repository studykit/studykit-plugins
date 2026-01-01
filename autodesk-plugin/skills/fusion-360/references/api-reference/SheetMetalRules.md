# SheetMetalRules Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/SheetMetalRules.h>

## Description

A collection of sheet metal rules.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [addByCopy](SheetMetalRules_addByCopy.htm) | Creates a new sheet metal rule by copying an existing rule. The new rule can then be edited to define the rule characteristics you want. |
| [classType](SheetMetalRules_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](SheetMetalRules_item.htm) | Function that returns the specified sheet metal rule using an index into the collection. |
| [itemByName](SheetMetalRules_itemByName.htm) | Function that returns the specified sheet metal rule using the name of the rule. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](SheetMetalRules_count.htm) | The number of sheet metal rules in the collection. |
| [isValid](SheetMetalRules_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](SheetMetalRules_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[Design.designSheetMetalRules](Design_designSheetMetalRules.htm), [Design.librarySheetMetalRules](Design_librarySheetMetalRules.htm), [FlatPatternProduct.designSheetMetalRules](FlatPatternProduct_designSheetMetalRules.htm), [FlatPatternProduct.librarySheetMetalRules](FlatPatternProduct_librarySheetMetalRules.htm), [WorkingModel.designSheetMetalRules](WorkingModel_designSheetMetalRules.htm), [WorkingModel.librarySheetMetalRules](WorkingModel_librarySheetMetalRules.htm)

## Version

Introduced in version November 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |