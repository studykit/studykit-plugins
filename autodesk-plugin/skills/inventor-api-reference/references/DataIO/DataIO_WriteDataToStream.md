# DataIO.WriteDataToStream Method

Parent Object: [DataIO](../DataIO/DataIO.md)

## Description

Writes out the contents of the supporting object in the specified format onto a Stream (IStream). If once-dereferenced Stream pointer is NULL, then a Stream is allocated and must be 'Release-d()' by caller.

## Syntax

DataIO.**WriteDataToStream**( ***Format*** As String, ***Stream*** As Unknown )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Format | String | Input String that specifies the format of the data to be written to the stream. |
| Stream | Unknown | Input/output object from which to read the formatted data. |

## Version

Introduced in version 4
