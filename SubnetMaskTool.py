import array
import ipaddress

ipaddr = input("What is the main Network IP Address?")

Subnets = input("How many subnets do you want to create?")

Netty = []
Ranges = []
BroadcastAddresses = []

def AvailableNetworks():
    NetArray = [2, 4, 16, 32, 64, 128, 256]
    HostArry = [256, 128, 64, 32, 16, 8, 4, 2]
    for i in NetArray:
        if i >= int(SubnetsDesired):
            NumbSubnets = i
            SubnetIndex = NetArray.index(i)
            NumIps = HostArry[SubnetIndex + 1]
            joinedips = MainNetwork.split(".")
            joinedips = list(map(int, joinedips))
            for i in range(NumbSubnets - 1)
                joinedips[-1] += NumIps
                GoodNets.append('.'.join(str(i) for i in joinedips))
                break


def SubnetRanges():
    NetArray = [2, 4, 8, 16, 32, 64, 128, 256]
    HostArray = [256, 128, 64, 32, 16, 8, 4, 2]
    joinedips = MainNetwork.split(".")
    joinedips = list(map(int, joinedips))
    for i in NetArray:
        if i >= int(SubnetsDesired):
            NumbSubnets = i
            SubnetIndex = NetArray.index(i)
            NumbIps = HostArray[SubnetIndex +1]
            for i in range(NumbSubnets -1)
                Range = "." + str(joinedips[-1] + 1) + "-" + "." + str(joinedips[-1] + NumIps -2)
                Ranges.append(Range)
                joinedips[-1] += NumbIp
            break


def BroadcastAddy():
    NetArray = [2, 4, 8, 16, 32, 64, 128, 256]
    HostArray = [256, 128, 64, 32, 16, 8, 4, 2]
    for i in NetArray:
        if i >= int(SubnetsDesired):
            NumbSubnets = i
            SubnetIndex = NetArray.index(i)
            NumIps = HostArray[SubnetIndex + 1]
            ipaddy = MainNetwork.split(".")
            ipaddy = list(map(int, ipaddy))
            for i in range(NumbSubnets - 1):
                ipaddy[-1] += NumIps -1
                BroadcastAddresses.append('.'.join(str(i) for i in ipaddy))
                ipaddy[-1] += 1
            break

def Cider():
    NetArray = [2, 4, 8, 16, 32, 64, 128, 256]
    ciderlist = ["/25", "/26", "/27", "/28", "/29", "/30", "/31", "/32"]
    for i in NetArray:
        if i >= int(SubnetsDesired):
            CiderIndex = NetArray.index(i)
            print("CIDR Notation:", ciderlist[CiderIndex])
            break

def SubNetMask():
    NetArray = [2, 4, 8, 16, 32, 64, 128, 256]
    MaskValues = [128, 64, 32, 16, 8, 4, 2, 1]
    BitValue = 0
    MaskIndex = 0
    for i in NetArray:
        if i >= int(SubnetsDesired):
            MaskIndex = NetArray.index(i)
            break
    for i in range(MaskIndex):
        BitValue += MaskValues[i]
    print("Subnet Mask:", '255.255.255.' + str(BitValue))

if __name__== '__main__':
    AvailableNetworks()
    SubnetRanges()
    BroadcastAddy()


 FinalReport = zip(GoodNets, Ranges, BroadcastAddresses)
formatted = "{:<30}{:<30}{:<30}"

print(formatted.format("Network ID", "Range", "Broadcast Address"))
for list in FinalReport:
        print(formatted.format(list[0], list[1], list[2]))

print()
Cider()
print()
SubNetMask()
