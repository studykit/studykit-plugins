# PlasticRules Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Plastic/PlasticRules.h>

## Description

A collection of plastic rules.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [addByCopy](PlasticRules_addByCopy.htm) | Creates a new plastic rule by copying an existing rule. The new rule can then be edited to define the rule characteristics you want. |
| [classType](PlasticRules_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](PlasticRules_item.htm) | Function that returns the specified plastic rule using an index into the collection. |
| [itemByName](PlasticRules_itemByName.htm) | Function that returns the specified plastic rule using the name of the rule. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](PlasticRules_count.htm) | The number of plastic rules in the collection. |
| [isValid](PlasticRules_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](PlasticRules_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[Design.designPlasticRules](Design_designPlasticRules.htm), [Design.libraryPlasticRules](Design_libraryPlasticRules.htm), [FlatPatternProduct.designPlasticRules](FlatPatternProduct_designPlasticRules.htm), [FlatPatternProduct.libraryPlasticRules](FlatPatternProduct_libraryPlasticRules.htm), [WorkingModel.designPlasticRules](WorkingModel_designPlasticRules.htm), [WorkingModel.libraryPlasticRules](WorkingModel_libraryPlasticRules.htm)

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |