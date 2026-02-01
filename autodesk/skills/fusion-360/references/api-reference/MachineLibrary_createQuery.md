# MachineLibrary.createQuery Method

Parent Object: [MachineLibrary](MachineLibrary.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachineLibrary.h>

## Description

Creates a new MachineQuery that is used to query the library for machines matching the query.

## Syntax

* [Python](#Python)
* [C++](#C++)

"machineLibrary\_var" is a variable referencing a [MachineLibrary](MachineLibrary.htm) object.```` ``` # Uses no optional arguments. ``` ```` |

"machineLibrary\_var" is a variable referencing a [MachineLibrary](MachineLibrary.htm) object.  ```` ``` #include <Cam/Machine/MachineLibrary.h>  // Uses no optional arguments. returnValue = machineLibrary_var->createQuery(location);  // Uses optional arguments. returnValue = machineLibrary_var->createQuery(location, vendor, model); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [MachineQuery](MachineQuery.htm) | Returns a new MachineQuery. The query is predefined by given parameter. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| location | [LibraryLocations](LibraryLocations.htm) | The location specifies the LibraryLocations where to search for in the machine library. |
| vendor | string | The vendor specifies the vendor of the machine. The default empty vendor applies to all machines.   This is an optional argument whose default value is "". |
| model | string | The model specifies the model of the machine. The default empty model applies to all machines.   This is an optional argument whose default value is "". |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |