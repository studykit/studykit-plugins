# CustomGraphicsGroups Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Graphics/CustomGraphicsGroups.h>

## Description

Provides access to a set of graphics groups that are either associated with a component or owned by another CustomGraphicsGroup object. This object also supports the creation of new custom graphics groups.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](CustomGraphicsGroups_add.htm) | Creates a new, empty CustomGraphicsGroup. |
| [classType](CustomGraphicsGroups_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](CustomGraphicsGroups_item.htm) | Function that returns the specified graphics group using an index into the collection. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](CustomGraphicsGroups_count.htm) | Returns the number of graphics groups in the collection. |
| [isValid](CustomGraphicsGroups_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](CustomGraphicsGroups_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[CAM.customGraphicsGroups](CAM_customGraphicsGroups.htm), [Component.customGraphicsGroups](Component_customGraphicsGroups.htm), [FlatPatternComponent.customGraphicsGroups](FlatPatternComponent_customGraphicsGroups.htm)

## Version

Introduced in version September 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |