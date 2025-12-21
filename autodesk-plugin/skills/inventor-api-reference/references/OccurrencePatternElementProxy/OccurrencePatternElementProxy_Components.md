# OccurrencePatternElementProxy.Components Property

Parent Object: [OccurrencePatternElementProxy](../OccurrencePatternElementProxy/OccurrencePatternElementProxy.md)

## Description

Property that returns the set of components that were created for this particular instance. There are cases where this collection can contain a count of zero. The obvious cases are when this element has been set to be independent or suppressed. There is another case when this element is the result of a feature based occurrence pattern and the instance it is associated with within the feature pattern has been suppressed.

## Syntax

OccurrencePatternElementProxy.**Components**() As [ObjectsEnumerator](../ObjectsEnumerator/ObjectsEnumerator.md)

## Property Value

This is a read only property whose value is an [ObjectsEnumerator](../ObjectsEnumerator/ObjectsEnumerator.md).

## Version

Introduced in version 2010
