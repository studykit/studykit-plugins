# KinematicsMachineElement Object

Derived from: [MachineElement](MachineElement.htm) Object

Defined in namespace "adsk::cam" and the header file is <Cam/Machine/KinematicsMachineElement.h>

## Description

Machine element representing the machine's kinematics tree.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](KinematicsMachineElement_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [staticTypeId](KinematicsMachineElement_staticTypeId.htm) | Identifying name for all elements of this type. Pass this to the itemByType or itemById methods of MachineElements to filter to elements of this type. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [elementId](KinematicsMachineElement_elementId.htm) | Identifier for this element. Unique within an element type. |
| [isValid](KinematicsMachineElement_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](KinematicsMachineElement_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [parts](KinematicsMachineElement_parts.htm) | Get the root parts collection. |
| [typeId](KinematicsMachineElement_typeId.htm) | Identifier for this type of machine element. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |