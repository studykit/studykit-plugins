# AdditiveFFFLimitsMachineElement Object

Derived from: [MachineElement](MachineElement.htm) Object

Defined in namespace "adsk::cam" and the header file is <Cam/Machine/AdditiveFFFLimitsMachineElement.h>

## Description

Machine element representing limits for fused filament fabrication (FFF) machine motion and temperatures.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](AdditiveFFFLimitsMachineElement_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [staticTypeId](AdditiveFFFLimitsMachineElement_staticTypeId.htm) | Identifying name for all elements of this type. Pass this to the itemByType or itemById methods of MachineElements to filter to elements of this type. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [elementId](AdditiveFFFLimitsMachineElement_elementId.htm) | Identifier for this element. Unique within an element type. |
| [homePosition](AdditiveFFFLimitsMachineElement_homePosition.htm) | Position of the machine home location. |
| [isValid](AdditiveFFFLimitsMachineElement_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [maximumBedTemperature](AdditiveFFFLimitsMachineElement_maximumBedTemperature.htm) | Maximum bed temperature in degrees C. |
| [maximumXYAcceleration](AdditiveFFFLimitsMachineElement_maximumXYAcceleration.htm) | Maximum supported acceleration for motion in the X or Y axes in cm/s^2. |
| [maximumXYSpeed](AdditiveFFFLimitsMachineElement_maximumXYSpeed.htm) | Maximum supported speed for motion in the X or Y axes in cm/s. |
| [maximumZAcceleration](AdditiveFFFLimitsMachineElement_maximumZAcceleration.htm) | Maximum supported acceleration for motion in the Z axis in cm/s^2. |
| [maximumZSpeed](AdditiveFFFLimitsMachineElement_maximumZSpeed.htm) | Maximum supported speed for motion in the Z axis in cm/s. |
| [objectType](AdditiveFFFLimitsMachineElement_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [parkPosition](AdditiveFFFLimitsMachineElement_parkPosition.htm) | Position machine moves to when "parked". |
| [typeId](AdditiveFFFLimitsMachineElement_typeId.htm) | Identifier for this type of machine element. |

## Version

Introduced in version July 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |