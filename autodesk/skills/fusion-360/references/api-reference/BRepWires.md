# BRepWires Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepWires.h>

## Description

Provides access to B-Rep wire bodies.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](BRepWires_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](BRepWires_item.htm) | Function that returns the specified wire using an index into the collection. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](BRepWires_count.htm) | The number of B-Rep wire bodies in the collection. |
| [isValid](BRepWires_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](BRepWires_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[BRepBody.wires](BRepBody_wires.htm)

## Version

Introduced in version December 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |