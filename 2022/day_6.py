"""
--- Day 6: Tuning Trouble ---
"""
import general as g
# packet = g.read_file("test_input.txt")
packet = g.read_file()


def get_payload(packet: str, marker_length: int) -> int:
    """Quick put together solution"""
    for count, _ in enumerate(packet):
        slice = packet[count:count + marker_length]
        if len(slice) < marker_length:
            return -1
        
        ans = set(slice)
        if len(ans) == marker_length:
            # print("---")
            # print(slice)
            # print(count + marker_length)
            return count + marker_length


def main():
    # part one, start-of-packet marker
    print(get_payload(packet, 4))
    
    # part 2, start-of-message marker
    print(get_payload(packet, 14))


main()
