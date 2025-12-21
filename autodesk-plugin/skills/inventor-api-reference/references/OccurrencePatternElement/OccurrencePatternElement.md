# OccurrencePatternElement Object

## Description

The OccurrencePatternElement object represents a single instance within an occurrence pattern.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../OccurrencePatternElement/OccurrencePatternElement_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Components](../OccurrencePatternElement/OccurrencePatternElement_Components.md) | Property that returns the set of components that were created for this particular instance. There are cases where this collection can contain a count of zero. The obvious cases are when this element has been set to be independent or suppressed. There is another case when this element is the result of a feature based occurrence pattern and the instance it is associated with within the feature pattern has been suppressed. |
| [Independent](../OccurrencePatternElement/OccurrencePatternElement_Independent.md) | Gets/Sets whether the element is independent of the pattern or not. |
| [Index](../OccurrencePatternElement/OccurrencePatternElement_Index.md) | Property that returns the index of this element within the OccurrencePatternElements collection it is a member of. |
| [Name](../OccurrencePatternElement/OccurrencePatternElement_Name.md) | Property that returns the name of the element. |
| [Occurrences](../OccurrencePatternElement/OccurrencePatternElement_Occurrences.md) | Property that returns the set of occurrences that were created for this particular instance. |
| [Parent](../OccurrencePatternElement/OccurrencePatternElement_Parent.md) | Property that returns the parent occurrence pattern of the object. |
| [Suppressed](../OccurrencePatternElement/OccurrencePatternElement_Suppressed.md) | Gets/Sets whether the element is suppressed or not. |
| [Type](../OccurrencePatternElement/OccurrencePatternElement_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[CircularOccurrencePattern.PatternElement](../CircularOccurrencePattern/CircularOccurrencePattern_PatternElement.md), [CircularOccurrencePatternProxy.PatternElement](../CircularOccurrencePatternProxy/CircularOccurrencePatternProxy_PatternElement.md), [ComponentOccurrence.PatternElement](../ComponentOccurrence/ComponentOccurrence_PatternElement.md), [ComponentOccurrenceProxy.PatternElement](../ComponentOccurrenceProxy/ComponentOccurrenceProxy_PatternElement.md), [FeatureBasedOccurrencePattern.PatternElement](../FeatureBasedOccurrencePattern/FeatureBasedOccurrencePattern_PatternElement.md), [FeatureBasedOccurrencePatternProxy.PatternElement](../FeatureBasedOccurrencePatternProxy/FeatureBasedOccurrencePatternProxy_PatternElement.md), [OccurrencePattern.PatternElement](../OccurrencePattern/OccurrencePattern_PatternElement.md), [OccurrencePatternElementProxy.NativeObject](../OccurrencePatternElementProxy/OccurrencePatternElementProxy_NativeObject.md), [OccurrencePatternElements.Item](../OccurrencePatternElements/OccurrencePatternElements_Item.md), [RectangularOccurrencePattern.OccurrencePatternElement](../RectangularOccurrencePattern/RectangularOccurrencePattern_OccurrencePatternElement.md), [RectangularOccurrencePattern.PatternElement](../RectangularOccurrencePattern/RectangularOccurrencePattern_PatternElement.md), [RectangularOccurrencePatternProxy.OccurrencePatternElement](../RectangularOccurrencePatternProxy/RectangularOccurrencePatternProxy_OccurrencePatternElement.md), [RectangularOccurrencePatternProxy.PatternElement](../RectangularOccurrencePatternProxy/RectangularOccurrencePatternProxy_PatternElement.md)

## Derived Classes

[OccurrencePatternElementProxy](../OccurrencePatternElementProxy/OccurrencePatternElementProxy.md)

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |