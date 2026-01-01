# TangentRelationships Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/TangentRelationships.h>

## Description

The collection of Tangent Relationships in this component. This provides access to all existing tangent relationships and supports the ability to create new tangent relationships.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](TangentRelationships_add.htm) | Creates a new tangent relationship between two components. |
| [classType](TangentRelationships_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createInput](TangentRelationships_createInput.htm) | Creates a TangentRelationshipInput object, which is the API equivalent to the Tangent Relationship command dialog. You use methods and properties on the returned class to set the desired options, similar to providing input in the Tangent Relationship command dialog. Once the settings are defined you call the TangentRelationships.add method passing in the TangentRelationshipInput object to create the actual TangentRelationship. |
| [item](TangentRelationships_item.htm) | Function that returns the specified tangent relationship using an index into the collection. |
| [itemByName](TangentRelationships_itemByName.htm) | Function that returns the specified tangent relationship using a name. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](TangentRelationships_count.htm) | Returns number of TangentRelationship objects in the collection. |
| [isValid](TangentRelationships_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](TangentRelationships_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[Component.tangentRelationships](Component_tangentRelationships.htm), [FlatPatternComponent.tangentRelationships](FlatPatternComponent_tangentRelationships.htm)

## Version

Introduced in version May 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |