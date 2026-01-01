# MachineAvoidSelectionBase Object

Derived from: [GeometrySelection](GeometrySelection.htm) Object

Defined in namespace "adsk::cam" and the header file is <Cam/MachineAvoidSelections/MachineAvoidSelectionBase.h>

## Description

Base parent class for all machine/avoid selection classes.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](MachineAvoidSelectionBase_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [axialOffset](MachineAvoidSelectionBase_axialOffset.htm) | Axial offset - sets the corresponding axial offset value based on the machine mode |
| [combinedOffset](MachineAvoidSelectionBase_combinedOffset.htm) | Combined offset - clearance and stock to leave based on the machine mode This only applies to strategies that use a single offset value (Advanced Swarf, Multi-Axis Clearing, Multi-Axis Finishing, Deburr and Geodesic) |
| [error](MachineAvoidSelectionBase_error.htm) | Gets the last warning string encountered after the selection was applied to a parent. |
| [hasError](MachineAvoidSelectionBase_hasError.htm) | Gets if errors were encountered when applying the selection to a a parent. |
| [hasWarning](MachineAvoidSelectionBase_hasWarning.htm) | Gets if warnings were encountered when applying the selection to a parent. |
| [isValid](MachineAvoidSelectionBase_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [machineMode](MachineAvoidSelectionBase_machineMode.htm) | Desired machining mode. The default is Avoid. The current machining mode will determine which value the radial and axial offset functions refer to. When set to Machine, the radial and axial offset methods will read/set the stock to leave parameter. When set to Avoid, the radial and axial offset methods will read/set the clearance value, and the Fixture mode will map to the relative fixture clearance value. |
| [objectType](MachineAvoidSelectionBase_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [radialOffset](MachineAvoidSelectionBase_radialOffset.htm) | Radial offset - sets the corresponding radial offset value based on the machine mode |
| [value](MachineAvoidSelectionBase_value.htm) | Returns the resulting value of the selection. In general, this returns the input selection, but child classes can override the return value if needed. Refer to the child classes comments for further details. The collection may contain duplicates. For OperationInputs, the return value may not be the same as for Operations, as additional geometry selected by child classes is not evaluated for OperationInputs. |
| [warning](MachineAvoidSelectionBase_warning.htm) | Gets the last warning string encountered after the selection was applied to a parent. |

## Accessed From

[MachineAvoidGroups.defaultGroup](MachineAvoidGroups_defaultGroup.htm), [MachineAvoidGroups.item](MachineAvoidGroups_item.htm)

## Derived Classes

[MachineAvoidDefaultSelection](MachineAvoidDefaultSelection.htm), [MachineAvoidDirectSelection](MachineAvoidDirectSelection.htm)

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |