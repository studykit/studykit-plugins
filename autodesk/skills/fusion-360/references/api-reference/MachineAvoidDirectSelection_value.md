# MachineAvoidDirectSelection.value Property

Parent Object: [MachineAvoidDirectSelection](MachineAvoidDirectSelection.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/MachineAvoidSelections/MachineAvoidDirectSelection.h>

## Description

Returns the resulting value of the selection. In general, this returns the input selection, but child classes can override the return value if needed. Refer to the child classes comments for further details. The collection may contain duplicates. For OperationInputs, the return value may not be the same as for Operations, as additional geometry selected by child classes is not evaluated for OperationInputs.

## Syntax

* [Python](#Python)
* [C++](#C++)

"machineAvoidDirectSelection\_var" is a variable referencing a MachineAvoidDirectSelection object. |

"machineAvoidDirectSelection\_var" is a variable referencing a MachineAvoidDirectSelection object. ```` ``` #include <Cam/MachineAvoidSelections/MachineAvoidDirectSelection.h>  // Get the value of the property. std::vector<Ptr<Base>> propertyValue = machineAvoidDirectSelection_var->value(); ``` ```` |

## Property Value

This is a read only property whose value is an array of type [Base](Base.htm).

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |