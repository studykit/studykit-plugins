# ThreadFeatures.createInput Method

Parent Object: [ThreadFeatures](ThreadFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ThreadFeatures.h>

## Description

Creates a ThreadFeatureInput object. This object is the API equivalent of the Thread feature dialog. It collects the required input and once fully defined you can pass this object to the ThreadFeatures.add method to create the thread feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"threadFeatures\_var" is a variable referencing a [ThreadFeatures](ThreadFeatures.htm) object.```` ``` returnValue = threadFeatures_var.createInput(inputCylindricalFaces, threadInfo) ``` ```` |

"threadFeatures\_var" is a variable referencing a [ThreadFeatures](ThreadFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ThreadFeatureInput](ThreadFeatureInput.htm) | Returns the newly created ThreadFeatureInput object or null/None if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputCylindricalFaces | [Base](Base.htm) | A single cylindrical BRep face or a collection of cylindrical BRep faces to thread. A collection of faces must all be from either holes (for internal threading) or all from cylinders (for external threading). Both internal and external threads cannot be created in the same feature. The faces in a collection can come from different bodies or components. |
| threadInfo | [ThreadInfo](ThreadInfo.htm) | The ThreadInfo object that defines the type and size of the thread to create. When creating a thread, the type and size of the thread is specified by referencing thread information defined in one of the XML files in the ThreadData folder within the Fusion install folder. You can use the ThreadDataQuery object to query these XML files to find the specific thread you want to create. The ThreadDataQuery object can be obtained by using the ThreadFeatures.threadDataQuery property. You then use this information to create a ThreadInfo object using the ThreadFeatures.createThreadInfo method. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Thread Feature API Sample](ThreadFeatureSample_Sample.htm) | Demonstrates creating a new thread feature. |

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |