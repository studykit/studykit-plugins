# ModelParameters Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/ModelParameters.h>

## Description

Provides access to the Model Parameters within a component.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](ModelParameters_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](ModelParameters_item.htm) | Function that returns the specified Model Parameter using an index into the collection. |
| [itemByName](ModelParameters_itemByName.htm) | Function that returns the specified Model Parameter using the name of the parameter as it is displayed in the parameters dialog. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [component](ModelParameters_component.htm) | Returns the component that owns the Model Parameters collection |
| [count](ModelParameters_count.htm) | Returns the number of parameters in the collection. |
| [isValid](ModelParameters_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](ModelParameters_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[Component.modelParameters](Component_modelParameters.htm), [CustomFeatureParameter.modelParameters](CustomFeatureParameter_modelParameters.htm), [FlatPatternComponent.modelParameters](FlatPatternComponent_modelParameters.htm), [ModelParameter.modelParameters](ModelParameter_modelParameters.htm)

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |