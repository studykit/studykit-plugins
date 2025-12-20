# ComponentOccurrenceProxy.GetDegreesOfFreedom Method

Parent Object: [ComponentOccurrenceProxy](../ComponentOccurrenceProxy/ComponentOccurrenceProxy.md)

## Description

Method that returns the available degrees of freedom for the occurrence.

## Syntax

ComponentOccurrenceProxy.**GetDegreesOfFreedom**( ***TranslationDegreesCount*** As Long, ***TranslationDegreesVectors*** As [ObjectsEnumerator](../ObjectsEnumerator/ObjectsEnumerator.md), ***RotationDegreesCount*** As Long, ***RotationDegreesVectors*** As [ObjectsEnumerator](../ObjectsEnumerator/ObjectsEnumerator.md), ***DOFCenter*** As [Point](../Point/Point.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| TranslationDegreesCount | Long | Output Long that returns the number of available translational degrees of freedom. The value can be from 0 to 3. |
| TranslationDegreesVectors | [ObjectsEnumerator](../ObjectsEnumerator/ObjectsEnumerator.md) | Output ObjectsEnumerator that returns Vector objects corresponding to the available translational degrees of freedom. |
| RotationDegreesCount | Long | Output Long that returns the number of available rotational degrees of freedom. The value can be from 0 to 3. |
| RotationDegreesVectors | [ObjectsEnumerator](../ObjectsEnumerator/ObjectsEnumerator.md) | Output ObjectsEnumerator that returns Vector objects corresponding to the available rotational degrees of freedom. |
| DOFCenter | [Point](../Point/Point.md) | Output Point object that returns the DOF center as displayed by Inventor. |

## Version

Introduced in version 2008

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |