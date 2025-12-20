# AssemblyJointsEnumerator.Item Property

Parent Object: [AssemblyJointsEnumerator](../AssemblyJointsEnumerator/AssemblyJointsEnumerator.md)

## Description

Method that returns the specified AssemblyJoint object from the collection. This is the default method of the AssemblyJointsEnumerator collection object.

## Syntax

AssemblyJointsEnumerator.**Item**( ***Index*** As Variant ) As [AssemblyJoint](../AssemblyJoint/AssemblyJoint.md)

## Property Value

This is a read only property whose value is an [AssemblyJoint](../AssemblyJoint/AssemblyJoint.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the AssemblyJoint to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the joint name. The name expected is the display name of the joint. This is the name that is displayed to the user in the assembly browser. If an out of range index or a name of a non-existent joint name is provided, an error occurs. |

## Version

Introduced in version 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |