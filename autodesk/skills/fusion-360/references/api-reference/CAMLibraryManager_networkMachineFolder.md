# CAMLibraryManager.networkMachineFolder Property

Parent Object: [CAMLibraryManager](CAMLibraryManager.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Global/CAMLibraryManager.h>

## Description

Gets the absolute path to the folder containing network machines. Network machines appear in the machine library under the network tab.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMLibraryManager\_var" is a variable referencing a CAMLibraryManager object. |

"cAMLibraryManager\_var" is a variable referencing a CAMLibraryManager object. ```` ``` #include <Cam/Global/CAMLibraryManager.h>  // Get the value of the property. string propertyValue = cAMLibraryManager_var->networkMachineFolder(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |