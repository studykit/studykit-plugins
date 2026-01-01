# MachineElement Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachineElement.h>

## Description

Base class for objects that compose a machine.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](MachineElement_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [elementId](MachineElement_elementId.htm) | Identifier for this element. Unique within an element type. |
| [isValid](MachineElement_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](MachineElement_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [typeId](MachineElement_typeId.htm) | Identifier for this type of machine element. |

## Accessed From

[MachineElements.addElement](MachineElements_addElement.htm), [MachineElements.defaultItemByType](MachineElements_defaultItemByType.htm), [MachineElements.item](MachineElements_item.htm), [MachineElements.itemById](MachineElements_itemById.htm), [MachineElements.itemsByType](MachineElements_itemsByType.htm)

## Derived Classes

[AdditiveFFFLimitsMachineElement](AdditiveFFFLimitsMachineElement.htm), [AdditivePlatformMachineElement](AdditivePlatformMachineElement.htm), [ControllerConfigurationMachineElement](ControllerConfigurationMachineElement.htm), [InteractionsMachineElement](InteractionsMachineElement.htm), [KinematicsMachineElement](KinematicsMachineElement.htm), [MultiAxisMachineElement](MultiAxisMachineElement.htm), [PostProcessingMachineElement](PostProcessingMachineElement.htm), [ToolingCapabilitiesMachineElement](ToolingCapabilitiesMachineElement.htm)

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |