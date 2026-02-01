# ShellFeatures.createInput Method

Parent Object: [ShellFeatures](ShellFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ShellFeatures.h>

## Description

Creates a ShellFeatureInput object. Use properties and methods on this object to define the shell you want to create and then use the Add method, passing in the ShellFeatureInput object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"shellFeatures\_var" is a variable referencing a [ShellFeatures](ShellFeatures.htm) object.```` ``` # Uses no optional arguments. ``` ```` |

"shellFeatures\_var" is a variable referencing a [ShellFeatures](ShellFeatures.htm) object.  ```` ``` #include <Fusion/Features/ShellFeatures.h>  // Uses no optional arguments. returnValue = shellFeatures_var->createInput(inputEntities);  // Uses optional arguments. returnValue = shellFeatures_var->createInput(inputEntities, isTangentChain); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ShellFeatureInput](ShellFeatureInput.htm) | Returns the newly created ShellFeatureInput object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputEntities | [ObjectCollection](ObjectCollection.htm) | The collection contains the faces to remove and the bodies to perform shell. Fails if any faces are input, and the owning bodies of the faces are also input. |
| isTangentChain | boolean | A boolean value for setting whether or not faces that are tangentially connected to the input faces (if any) will also be included. It defaults to true.   This is an optional argument whose default value is True. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [shellFeatures.add](shelFeatures_add_Sample.htm) | Demonstrates creating a shell feature. |
| [Shell Feature API Sample](ShellFeatureSample_Sample.htm) | Demonstrates creating a new shell feature. |

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |