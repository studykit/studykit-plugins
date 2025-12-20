# TaperedThreadInfo Object

Derived from: [ThreadInfo](../ThreadInfo/ThreadInfo.md) Object

## Description

The TaperedThreadInfo object defines the thread information that is used by the Hole and Thread features. For standard threads the StandardThreadInfo object is used.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../TaperedThreadInfo/TaperedThreadInfo_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [BasicMinorDiameter](../TaperedThreadInfo/TaperedThreadInfo_BasicMinorDiameter.md) | Property that returns s the basic minor diameter, or the diameter of the small end of the pipe. This is in millimeters if the Metric argument is True and inches if False. This property contains a Double value or can be Nothing if the value is not set. |
| [CustomThreadDesignation](../TaperedThreadInfo/TaperedThreadInfo_CustomThreadDesignation.md) | Indicates the custom thread designation from the Custom Thread Designation column of the thread data spreadsheet. |
| [EffectiveDiameter](../TaperedThreadInfo/TaperedThreadInfo_EffectiveDiameter.md) | Property that returns the external effective thread diameter. This is in millimeters if the Metric argument is True and inches if False. This property contains a Double value or can be Nothing if the value is not set. |
| [EffectiveLength](../TaperedThreadInfo/TaperedThreadInfo_EffectiveLength.md) | Property that returns the external effective thread length. This is in millimeters if the Metric argument is True and inches if False. This property contains a Double value or can be Nothing if the value is not set. |
| [EngagementDiameter](../TaperedThreadInfo/TaperedThreadInfo_EngagementDiameter.md) | Property that returns the hand tight engagement diameter. This is in millimeters if the Metric argument is True and inches if False. This property contains a Double value or can be Nothing if the value is not set. |
| [EngagementLength](../TaperedThreadInfo/TaperedThreadInfo_EngagementLength.md) | Property that returns the hand tight engagement length. This is in millimeters if the Metric argument is True and inches if False. This property contains a Double value or can be Nothing if the value is not set. |
| [ExternalPitchDiameter](../TaperedThreadInfo/TaperedThreadInfo_ExternalPitchDiameter.md) | Property that returns the external pitch diameter. This is in millimeters if the Metric argument is True and inches if False. This property contains a Double value or can be Nothing if the value is not set. |
| [FullThreadDepth](../TaperedThreadInfo/TaperedThreadInfo_FullThreadDepth.md) | Gets whether this thread is the full length of the cylinder or cone. |
| [Internal](../TaperedThreadInfo/TaperedThreadInfo_Internal.md) | Gets and sets whether this is an internal thread or external (False). |
| [Metric](../TaperedThreadInfo/TaperedThreadInfo_Metric.md) | Gets and sets whether this thread is metric or not. |
| [NominalExternalDiameter](../TaperedThreadInfo/TaperedThreadInfo_NominalExternalDiameter.md) | Property that returns the nominal external diameter. This is in millimeters if the Metric argument is True and inches if False. This property contains a Double value or can be Nothing if the value is not set. |
| [NominalExternalLength](../TaperedThreadInfo/TaperedThreadInfo_NominalExternalLength.md) | Property that returns the nominal perfect external thread length. This is in millimeters if the Metric argument is True and inches if False. This property contains a Double value or can be Nothing if the value is not set. |
| [OutsidePipeDiameter](../TaperedThreadInfo/TaperedThreadInfo_OutsidePipeDiameter.md) | Property that returns the outside of the pipe diameter. This is in millimeters if the Metric argument is True and inches if False. This property contains a Double value or can be Nothing if the value is not set. |
| [OverallExternalLength](../TaperedThreadInfo/TaperedThreadInfo_OverallExternalLength.md) | Property that returns the overall external thread length. This is in millimeters if the Metric argument is True and inches if False. This property contains a Double value or can be Nothing if the value is not set. |
| [Pitch](../TaperedThreadInfo/TaperedThreadInfo_Pitch.md) | Property that returns the actual thread pitch. This value is used when displaying the threads in the model. This value is in millimeters if the Metric argument is True and inches if False. |
| [RightHanded](../TaperedThreadInfo/TaperedThreadInfo_RightHanded.md) | Gets and sets whether this is a right handed thread or left handed (False). |
| [TapDrillDiameter](../TaperedThreadInfo/TaperedThreadInfo_TapDrillDiameter.md) | Read-only property that returns the maximum pitch diameter. This is in millimeters if the Metric argument is True and inches if False. This property contains a Double value or can be Nothing if the value is not set. |
| [ThreadBasePoints](../TaperedThreadInfo/TaperedThreadInfo_ThreadBasePoints.md) | Property that returns an enumerator of Point objects indicating the base points for the thread. Typically, there is only one item in the collection. The exception is a hole feature based on multiple sketch points, in which case there are as many Point objects returned as there are sketch points. The point accounts for any offsets applied to the thread. The property returns a point only when the ThreadInfo object is obtained from a feature and returns Nothing in the forward create scenario. |
| [ThreadDesignation](../TaperedThreadInfo/TaperedThreadInfo_ThreadDesignation.md) | Property that returns a string that contains the thread designation. This is the full thread designation that is used in a drawing for the thread callout. |
| [ThreadDirection](../TaperedThreadInfo/TaperedThreadInfo_ThreadDirection.md) | Property that returns the direction of the thread. The property returns a vector only when the ThreadInfo object is obtained from a feature and returns Nothing in the forward create scenario. |
| [ThreadHeight](../TaperedThreadInfo/TaperedThreadInfo_ThreadHeight.md) | Property that returns the thread height. This is in millimeters if the Metric argument is True and inches if False. This property contains a Double value or can be Nothing if the value is not set. |
| [ThreadsPerInch](../TaperedThreadInfo/TaperedThreadInfo_ThreadsPerInch.md) | Property that returns a string that describes the pitch. This is generally described in threads per inch, although this string can contain any characters. This string is used as part of the text when a callout is created for the thread in a drawing. |
| [ThreadType](../TaperedThreadInfo/TaperedThreadInfo_ThreadType.md) | Gets and sets the thread type. |
| [ThreadTypeIdentifier](../TaperedThreadInfo/TaperedThreadInfo_ThreadTypeIdentifier.md) | Property that returns the string that identifies the thread type. This string is not localized and should not be changed by the user. The thread type is the name of the sheet in the Thread.xls file. |
| [Type](../TaperedThreadInfo/TaperedThreadInfo_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [VanishThread](../TaperedThreadInfo/TaperedThreadInfo_VanishThread.md) | Property that returns the vanish thread. This is in millimeters if the Metric argument is True and inches if False. This property contains a Double value or can be Nothing if the value is not set. |
| [WrenchMakeupDiameter](../TaperedThreadInfo/TaperedThreadInfo_WrenchMakeupDiameter.md) | Property that returns the internal wrench makeup diameter. This is in millimeters if the Metric argument is True and inches if False. This property contains a Double value or can be Nothing if the value is not set. |
| [WrenchMakeupLength](../TaperedThreadInfo/TaperedThreadInfo_WrenchMakeupLength.md) | Property that gets and sets the internal wrench makeup length. This is in millimeters if the Metric argument is True and inches if False. This property contains a Double value or can be Nothing if the value is not set. |

## Accessed From

[HoleFeatures.CreateTaperedTapInfo](../HoleFeatures/HoleFeatures_CreateTaperedTapInfo.md), [ThreadFeatures.CreateTaperedThreadInfo](../ThreadFeatures/ThreadFeatures_CreateTaperedThreadInfo.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Creating a ThreadInfo object](../../sample-programs/ThreadTableQuery_CreateThreadInfo_Sample.md) | Demonstrates the use of a ThreadInfo object. |

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |