# Decals Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Image/Decals.h>

## Description

Provides access to the Decals in a component and provides the functionality to add new Decals.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](Decals_add.htm) | Creates a new decal. Use the createInput method to first create an input object and set the available options. Then, pass that input object to the add method to create the decal. |
| [classType](Decals_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createInput](Decals_createInput.htm) | Creates a new DecalInput object. A DecalInput object is the logical equivalent to the Decal command dialog by providing access to all the decal options. Passing in the DecalInput object to the add method is the equivalent of clicking the OK button on the dialog to create the decal. |
| [item](Decals_item.htm) | Returns the specified Decal object using an index into the collection. |
| [itemByName](Decals_itemByName.htm) | Returns the specified decal using the name of the decal. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](Decals_count.htm) | Returns the number of decals in the component. |
| [isValid](Decals_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](Decals_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[BaseComponent.decals](BaseComponent_decals.htm), [Component.decals](Component_decals.htm), [FlatPatternComponent.decals](FlatPatternComponent_decals.htm)

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |