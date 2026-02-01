# MachineParts Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachineParts.h>

## Description

Object that represents a collection of machine parts. These parts are the children of another part or the collection of base parts from MachineKinematics.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](MachineParts_add.htm) | Add a new part to this collection. The part's parent will be set to the owner of this collection, or null if this is the root parts collection. |
| [classType](MachineParts_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createPartInput](MachineParts_createPartInput.htm) | Create a new MachinePartInput. |
| [item](MachineParts_item.htm) | Get the part at index in this collection. |
| [itemById](MachineParts_itemById.htm) | Get the part with the given ID. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](MachineParts_count.htm) | Get the number of parts in this collection. |
| [isValid](MachineParts_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](MachineParts_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |

## Accessed From

[KinematicsMachineElement.parts](KinematicsMachineElement_parts.htm), [MachinePart.children](MachinePart_children.htm)

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |