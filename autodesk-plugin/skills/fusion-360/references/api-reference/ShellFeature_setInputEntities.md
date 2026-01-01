# ShellFeature.setInputEntities Method

Parent Object: [ShellFeature](ShellFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ShellFeature.h>

## Description

Method that sets faces to remove and bodies to preform shell. Return false if any faces are input, and the owning bodies of the faces are also input.

## Syntax

* [Python](#Python)
* [C++](#C++)

"shellFeature\_var" is a variable referencing a [ShellFeature](ShellFeature.htm) object.```` ``` # Uses no optional arguments. returnValue = shellFeature_var.setInputEntities(inputEntities)  # Uses optional arguments. returnValue = shellFeature_var.setInputEntities(inputEntities, isTangentChain) ``` ```` |

"shellFeature\_var" is a variable referencing a [ShellFeature](ShellFeature.htm) object.  ```` ``` #include <Fusion/Features/ShellFeature.h>  // Uses no optional arguments. returnValue = shellFeature_var->setInputEntities(inputEntities);  // Uses optional arguments. returnValue = shellFeature_var->setInputEntities(inputEntities, isTangentChain); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if successful |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputEntities | [ObjectCollection](ObjectCollection.htm) | The collection contains the faces to remove and the bodies to perform shell. Fails if any faces are input, and the owning bodies of the faces are also input. |
| isTangentChain | boolean | A boolean value for setting whether or not faces that are tangentially connected to the input faces (if any) will also be included. It defaults to true.   This is an optional argument whose default value is True. |

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |