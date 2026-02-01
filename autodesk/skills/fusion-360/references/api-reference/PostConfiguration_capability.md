# PostConfiguration.capability Property

Parent Object: [PostConfiguration](PostConfiguration.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Post/PostConfiguration.h>

## Description

Gets the capabilities supported by the post. Capabilities define what types of operations can be post processed using this configuration.

## Syntax

* [Python](#Python)
* [C++](#C++)

"postConfiguration\_var" is a variable referencing a PostConfiguration object. |

"postConfiguration\_var" is a variable referencing a PostConfiguration object. ```` ``` #include <Cam/Post/PostConfiguration.h>  // Get the value of the property. PostCapabilities propertyValue = postConfiguration_var->capability(); ``` ```` |

## Property Value

This is a read only property whose value is a [PostCapabilities](PostCapabilities.htm).

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |