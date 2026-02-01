# CAMManager.networkMachineIntegrationManager Property

Parent Object: [CAMManager](CAMManager.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Global/CAMManager.h>

## Description

Gets the NetworkMachineIntegrationManager needed to integrate add-ins into the 'Find network machines' dialog.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMManager\_var" is a variable referencing a CAMManager object. |

"cAMManager\_var" is a variable referencing a CAMManager object. ```` ``` #include <Cam/Global/CAMManager.h>  // Get the value of the property. NetworkMachineIntegrationManager propertyValue = cAMManager_var->networkMachineIntegrationManager(); ``` ```` |

## Property Value

This is a read only property whose value is a NetworkMachineIntegrationManager.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |