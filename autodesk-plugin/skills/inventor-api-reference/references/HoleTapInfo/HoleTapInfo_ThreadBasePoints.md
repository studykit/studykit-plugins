# HoleTapInfo.ThreadBasePoints Property

Parent Object: [HoleTapInfo](../HoleTapInfo/HoleTapInfo.md)

## Description

Property that returns an enumerator of Point objects indicating the base points for the thread. Typically, there is only one item in the collection. The exception is a hole feature based on multiple sketch points, in which case there are as many Point objects returned as there are sketch points. The point accounts for any offsets applied to the thread. The property returns a point only when the ThreadInfo object is obtained from a feature and returns Nothing in the forward create scenario.

## Syntax

HoleTapInfo.**ThreadBasePoints**() As [ObjectsEnumerator](../ObjectsEnumerator/ObjectsEnumerator.md)

## Property Value

This is a read only property whose value is an [ObjectsEnumerator](../ObjectsEnumerator/ObjectsEnumerator.md).

## Version

Introduced in version 11

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |