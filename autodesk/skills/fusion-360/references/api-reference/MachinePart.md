# MachinePart Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachinePart.h>

## Description

Object representing some part of a machine, such as the static base of the machine, an axis, or the attachment points for tools and fixtures.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](MachinePart_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [deleteMe](MachinePart_deleteMe.htm) | Delete this part and its children from the kinematics tree. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [axis](MachinePart_axis.htm) | Get the axis object for this part used to reference this part for other operations. Only valid when partType is Axis, otherwise returns null |
| [children](MachinePart_children.htm) | Get the collection of child parts. |
| [id](MachinePart_id.htm) | Get the internal ID of the part. This is unique with respect to other MachineParts in the Machine. |
| [isValid](MachinePart_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](MachinePart_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [parent](MachinePart_parent.htm) | Get or set the parent of this part. Returns null if this part is a root part. Setting the parent will add this part to the end of the parent's children collection. Setting the parent will throw an error if the new parent is this part or a child of this part. |
| [partType](MachinePart_partType.htm) | Get the type of this part. |
| [spindle](MachinePart_spindle.htm) | Get the spindle object for this part used to reference this part for other operations. Will return null if the part has no spindle assigned. |
| [toolStation](MachinePart_toolStation.htm) | ![Preview](../images/TestTubeSmall.png)Get the tool station object for this part. Will return null if the part has no tool station assigned. |

## Accessed From

[MachineItem.part](MachineItem_part.htm), [MachinePart.parent](MachinePart_parent.htm), [MachineParts.add](MachineParts_add.htm), [MachineParts.item](MachineParts_item.htm), [MachineParts.itemById](MachineParts_itemById.htm)

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |