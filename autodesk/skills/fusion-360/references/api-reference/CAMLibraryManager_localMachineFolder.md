# CAMLibraryManager.localMachineFolder Property

Parent Object: [CAMLibraryManager](CAMLibraryManager.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Global/CAMLibraryManager.h>

## Description

This function is retired. See more information in the 'Remarks' section below.

## Remarks

This property has been retired. Please use the machine library to access machines instead.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMLibraryManager\_var" is a variable referencing a CAMLibraryManager object.  ```` ``` # Get the value of the property. propertyValue = cAMLibraryManager_var.localMachineFolder ``` ```` |

"cAMLibraryManager\_var" is a variable referencing a CAMLibraryManager object. ```` ``` #include <Cam/Global/CAMLibraryManager.h>  // Get the value of the property. string propertyValue = cAMLibraryManager_var->localMachineFolder(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version April 2023
Retired in version March 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |