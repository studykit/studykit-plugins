# StatusMessages.addWarning Method

Parent Object: [StatusMessages](StatusMessages.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/StatusMessages.h>

## Description

Adds a new warning status message to the list of warning and error messages.

## Syntax

* [Python](#Python)
* [C++](#C++)

"statusMessages\_var" is a variable referencing a [StatusMessages](StatusMessages.htm) object.```` ``` # Uses no optional arguments. ``` ```` |

"statusMessages\_var" is a variable referencing a [StatusMessages](StatusMessages.htm) object.  ```` ``` #include <Core/Application/StatusMessages.h>  // Uses no optional arguments. returnValue = statusMessages_var->addWarning();  // Uses optional arguments. returnValue = statusMessages_var->addWarning(messageId, message); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [StatusMessage](StatusMessage.htm) | Returns true if the warning message was successfully added. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| messageId | string | The ID of a predefined message or if an empty string is provided, the default error message will be used. The displayed message is localized based on the current default language in Fusion. Below is a list of some valid message ID's and the corresponding English message.    "API\_COMPUTE\_ERROR" - "Cannot compute this feature."  "API\_COMPUTE\_WARNING" - "This feature computed with warnings."  "CFLANGE\_INVALID\_GEOM" - "Invalid input sketch curve."  "DRAFT\_MISSING\_FACE\_REFERENCES" - "Missing face references"  "DRAFT\_MISSING\_REFERENCE\_PLANE" - "Missing reference plane"  "FEATURE\_ENTITY\_TYPE\_INVALID" - "Entity type is invalid"  "FEATURE\_FAILED\_TO\_CREATE" - "Failed to create feature"  "FEATURE\_MISSING\_INPUTS" - "Missing inputs"  "FEATURE\_REFERENCE\_LOST" - "Reference is lost"  "Feature\_Compute\_Error" - "Compute Failed"  "Feature\_Input\_Compute\_Error" - "Reference Failures"  "InvalidWPntInput" - "Invalid input"  "NO\_TARGET\_BODY" - "No target body!"  "ORIGIN\_SELECTION\_MISSING" - "Origin geometry is missing."  "DRPOINT\_COMPUTE\_FAILED" - "Failed to evaluate the point due to the invalid input"    This is an optional argument whose default value is "". |
| message | string | This is not currently supported for custom feature compute errors and will be ignored.   This is an optional argument whose default value is "". |

## Version

Introduced in version July 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |